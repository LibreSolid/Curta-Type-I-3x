"""Exercise the exported calculator page through the public viewer API.

Run `solid export -o _build_export` first. This opens an ephemeral loopback
server and headless browser, then closes both. Artifacts stay in _build_evidence.
"""

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from playwright.sync_api import sync_playwright


def check():
    root = Path(__file__).resolve().parents[2]
    assert (root / '_build_export/manifest.json').is_file(), 'Export the model first.'
    handler = partial(SimpleHTTPRequestHandler, directory=str(root))
    server = ThreadingHTTPServer(('127.0.0.1', 0), handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    errors = []
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True, args=[
                '--no-sandbox', '--disable-dev-shm-usage', '--use-angle=swiftshader',
                '--enable-unsafe-swiftshader'])
            page = browser.new_page(viewport={'width': 1200, 'height': 850})
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.goto(f'http://127.0.0.1:{server.server_port}/simulation/viewer/')
            page.wait_for_function('!!window.curta', timeout=120000)
            assert page.locator('canvas').first.bounding_box()['height'] > 500
            assert page.locator('#digits input').count() == 8

            for operand, result, turns in [(0, 0, 1), (1, 1, 2), (9, 10, 3), (90, 100, 4)]:
                page.locator('#operand').fill(str(operand))
                page.locator('#operand').press('Tab')
                page.locator('#crank').evaluate('e => {e.value=1; e.dispatchEvent(new Event("input"));}')
                assert page.locator('#result').inner_text() == str(result).zfill(11)
                assert page.locator('#turns').inner_text() == str(turns).zfill(6)
                page.locator('#commit').click()
                assert page.evaluate('curta.viewer.driver("crank_turns")') == 0
                assert page.evaluate('curta.viewer.driver("initial_result")') == result

            page.locator('#inside').click()
            assert not page.get_by_role('checkbox', name='Show enclosure', exact=True).is_checked()
            page.get_by_role('checkbox', name='Show enclosure', exact=True).check()
            page.get_by_role('checkbox', name='Show enclosure', exact=True).uncheck()
            page.evaluate('new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))')
            evidence = root / '_build_evidence'
            evidence.mkdir(exist_ok=True)
            page.screenshot(path=str(evidence / 'calculator-checked.png'),
                            timeout=180000, animations='disabled')
            assert not errors, errors
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
    print('Calculator page: calibration sequence, retained state, eight sliders, layer visibility and capture passed.')


if __name__ == '__main__':
    check()
