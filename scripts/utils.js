// Macron CLI helper functions

module.exports = {
  formatBytes: (bytes,decimals) => {
    if(bytes == 0) return '0 Bytes'
    
    let k = 1024,
      dm = decimals <= 0 ? 0 : decimals || 2,
      sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
      i = Math.floor(Math.log(bytes) / Math.log(k))
    
    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i]
  },
  copyFile: (source, target, cb) => {
    const { createReadStream, createWriteStream } = require('fs')
    let cbCalled = false;
    let rd = createReadStream(source);
    rd.on("error", function(err) {
      done(err);
    });
    let wr = createWriteStream(target);
    wr.on("error", function(err) {
      done(err);
    });
    wr.on("close", function(ex) {
      done();
    });
    rd.pipe(wr);
  
    function done(err) {
      if (!cbCalled) {
        cb(err);
        cbCalled = true;
      }
    }
  }
}