let socket = new WebSocket('ws://' + window.location.host + '/ws/products/')


socket.onmessage = function(event) {
    let test = event.data;
    console.log(test + "okay");


    var text = JSON.parse(event.data);
    let data = text.data

    // generating months and counts array out of object
    let result = data.reduce((c,v) => c.concat(v), []).map(o =>o.month);
    let results = data.reduce((c,v) => c.concat(v), []).map(o =>o.count);

    const dataUserCreated = {
        labels: Object.values(result),
        datasets: [{
            label: 'Users that have purchased products',
            backgroundColor: 'rgb(44, 189, 19)',
            borderColor: 'rgb(12, 61, 4)',
            data: Object.values(results)
        }]
    };

    const configUserCreated = {
        type: 'line',
        data: dataUserCreated,
        options: {}
    };

    // Creating new chart

    new Chart(
        document.getElementById('product-sales'),
        configUserCreated
    );
    
    };
    
    


let userPurchased = new WebSocket('ws://'+ window.location.host +'/ws/users-purchased/')

userPurchased.onmessage = function(event) {
    let data = event.data

    const dataUserPurchased = {
        labels: [
            'Total Users',
            'Total Purchased',
            'Purchased percentage'
        ],
        datasets: [{
            label: 'Users created',
            data: Object.values(data),
            backgroundColor: [
                'rgb(84, 4, 99)',
                'rgb(206, 24, 240)',
                'rgb(93, 57, 99)'
            ],
            hoverOffset: 4
        }]
    };


    const configUserPurchased = {
        type: 'pie',
        data: dataUserPurchased,
    };


    new Chart(
        document.getElementById('user-purchased'),
        configUserPurchased
    );
}

let userCreated = new WebSocket('ws://'+ window.location.host +'/ws/users-created/')

userCreated.onmessage = function (event) {
    let dat = JSON.parse(event.data)
    let data = dat.data;
    
    // generating months and counts array out of object
    let months = data.reduce((c,v) => c.concat(v), []).map(o =>o.month);
    let counts = data.reduce((c,v) => c.concat(v), []).map(o =>o.count);
    console.log(months,counts)
    

    const dataUserCreated = {
        labels: months,
        datasets: [{
            label: 'Users that have purchased products',
            backgroundColor: 'rgb(112, 6, 89)',
            borderColor: 'rgb(209, 8, 166)',
            data: counts,
        }]
    };

    const configUserCreated = {
        type: 'bar',
        data: dataUserCreated,
        options: {}
    };

    // Creating new chart

    new Chart(
        document.getElementById('user-created'),
        configUserCreated
    );
}
