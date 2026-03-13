function resolveUvGroup(engine, backend) {
    if (engine === "onnxruntime" && backend === "cuda") {
        return "onnxruntime-gpu";
    }
    if (engine === "onnxruntime" && backend === "directml") {
        return "onnxruntime-directml";
    }
    return engine;
}

async function recognize(_base64, lang, options) {
    const { config, utils } = options;
    const { run, cacheDir, osType, pluginDir } = utils;
    let { engine = "onnxruntime", backend = "auto", ocr = "PP-OCRv5" } = config
    const uvGroup = resolveUvGroup(engine, backend);
    let result = await run(`uv`, [
        `run`,
        `--group`,
        `${uvGroup}`,
        `${pluginDir}/main.py`,
        `${engine}`,
        `${ocr}`,
        `${backend}`,
        `${cacheDir}/pot_screenshot_cut.png`,
    ]);
    if (result.status === 0) {
        return result.stdout.trim();
    } else {
        throw Error(result.stderr);
    }
}
