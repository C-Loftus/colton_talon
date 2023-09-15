The purpose of the code in this folder is storing my Typescript functions I use to script actions that could normally not be done with Rango. Rango hints are not stable and can change on reload or window size, and as a result are not generally suitable for scripting chains of multiple actions in the browser, unless hint names are manually specified.

## Technical Details

This repository takes a sequence of Typescript files and outputs a series of Javascript files. This is done with webpack which allows us to minimize the size of the resulting Javascript. This is useful for when it is sent to the browser via the clipboard.

You will need `npm` and then run `npm install; npm run build` to compile the Typescript.

Chrome extensions cannot open a web server so we need to be able to send the Javascript an alternative way. Sending arbitrary javascript over a web socket is insecure

[https://luciopaiva.com/witchcraft/index.html](https://luciopaiva.com/witchcraft/index.html)
