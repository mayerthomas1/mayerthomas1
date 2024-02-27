var promise = new Promise(function(resolve, reject) {
    const x = "A tomato is a fruit";
    const y = "A tomato is a vegetable"
    if(x === y) {
        resolve();
    } else {
        reject();
    }
    });
    
    promise.
        then(function () {
            console.log('Tomatoes have seeds');
        }).
        catch(function () {
            console.log('A tomato is a vegetable of course!');
        });
    