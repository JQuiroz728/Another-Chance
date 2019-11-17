// One of my hopeless attempts of trying to integrate Python script into backend
let {PythonShell} = require('python-shell');
let pyShell = new PythonShell('s2t.py');

PythonShell.run('s2t.py', null, function(err, message) {
    if (err) {
        throw err;
    }
    console.log(message);

});

pyShell.on('message', function(message) {
    console.log(message);
});

pyShell.end(function(err) {
    if (err) {
        throw err;
    }
    
})