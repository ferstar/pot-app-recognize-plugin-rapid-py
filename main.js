async function recognize(_base64, lang, options) {
    const { config, utils } = options;
    const { run, cacheDir, osType, pluginDir } = utils;
    let { model = "with_onnx" } = config
    let exeName = "main.py";

    if (osType !== "Windows_NT") {
        let res = await run('chmod', ['+x', `${pluginDir}/${exeName}`]);
    }

    let result = await run(`${pluginDir}/${exeName}`, [
        `${model}`,
        `${cacheDir}/pot_screenshot_cut.png`,
    ]);
    if (result.status === 0) {
        return result.stdout.trim();
    } else {
        throw Error(result.stderr);
    }
}
