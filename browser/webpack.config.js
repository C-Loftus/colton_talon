const path = require("path");
const glob = require("glob");

module.exports = {
  target: "web",
  entry: glob
    .sync("./src/**/*.{ts,js}", { ignore: "./src/**/*.test.js" })
    .reduce((acc, file) => {
      acc[file.slice(3, -3)] = file;
      return acc;
    }, {}),
  output: {
    path: path.resolve(__dirname, "build"),
    filename: "[name].js",
    chunkFilename: "[name]-[id].js",
  },
  resolve: {
    extensions: [".ts", "..."],
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
        use: "ts-loader",
        exclude: "/node_modules/",
      },
    ],
  },
};
