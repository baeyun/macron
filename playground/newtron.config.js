module.exports = {
  name: "HelloWorldApplication",
  src: {
    uri: "http://localhost:3000/",
    html: "public/index.html"
  },
  nativeAPIsHandlerPath: "",
  logoPath: "assets/logos/",
  nativeAPI: [
    ".bin/NativeColorSwatch.py",
    "python/LoadStatusbarWhenAppReady.py"
  ]
}