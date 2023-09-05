const path = require('path');
const glob = require("glob");

module.exports = {
    target: "web",
    entry: glob.sync("./src/**/*.{js, ts,tsx}").reduce((acc, file) => {
        const relativePath = path.relative(__dirname, file); // Convert to relative path
        const parsedName = path.parse(relativePath).name; // get name and get rid of .ts extension
        acc[parsedName.replace(/^src[\/\\]/, "")] = file;
        return acc;
    }, {}),
    output: {
        filename: "[name].js",
        chunkFilename: "[name]-[id].js",
        path: __dirname + "/build"
    },
    resolve: {
        extensions: ['.ts', '...'],
        preferRelative: true,
    },
    module: {
        rules: [
            // {
            //     test: /\.css$/i,
            //     use: [
            //         'style-loader',
            //         'css-loader'
            //     ]
            // },
            {
                test: /\.ts$/i,
                use: 'ts-loader',
                exclude: '/node_modules/'
            }
        ]
    }
}