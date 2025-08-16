async function recognize(_base64, lang, options) {
    const { config, utils } = options;
    const { run, cacheDir, osType, pluginDir } = utils;
    let { engine = "onnxruntime", ocr = "PP-OCRv5" } = config
    let result = await run(`uv`, [
        `run`,
        `--group`,
        `${engine}`,
        `${pluginDir}/main.py`,
        `${engine}`,
        `${ocr}`,
        `${cacheDir}/pot_screenshot_cut.png`,
    ]);
    if (result.status === 0) {
        return result.stdout.trim();
    } else {
        throw Error(result.stderr);
    }
}
