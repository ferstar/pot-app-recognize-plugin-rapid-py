async function recognize(_base64, lang, options) {
    const { config, utils } = options;
    const { run, cacheDir, osType, pluginDir } = utils;
    let { model = "with_onnx" } = config
    let result = await run(`uv`, [
        `run`,
        `--group`,
        `${model}`,
        `${pluginDir}/main.py`,
        `${model}`,
        `${cacheDir}/pot_screenshot_cut.png`,
    ]);
    if (result.status === 0) {
        return result.stdout.trim();
    } else {
        throw Error(result.stderr);
    }
}
