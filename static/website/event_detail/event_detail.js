var event_detail = document.querySelector('#event_detail')
console.log(event_detail)

put_event_in_place = (event) => {
    event_detail.innerHTML += (`
            <div class="container">
                <div class='row justify-content-center'>
                    <div class='col-md-5 align-self-center d-flex justify-content-center'>                    
                        <img src='${event.cover_pic}'>
                    </div>
                    <div class='col-md-7'>                    
                        <h2 class="">${event.name}</h2>
                        <hr>
                        <p><strong>Date: </strong>${event.date}</p>
                        <p><strong>Time: </strong>${event.time}</p>
                        <p><strong>Email: </strong>${event.email}</p>
                        <p><strong>Venue: </strong>${event.venue} on ${event.date} at ${event.time}</p>
                        <p class="text-justify">${event.details}</p>
                    </div>
                </div>
            </div>
        `)
}

fetch('/events/list')
    .then(data => data.json())
    .then((data) => {
        // close the spinner
        document.querySelector('#spinner').remove()
        console.log(data);
        // put the data into place
        var page_eid = window.location.href.split('/').pop()
        var event = data.events.filter((event) => event.id == page_eid)[0]
        put_event_in_place(event)
        console.log(JSON.stringify(event, null, 2))

    })
    .catch(err => console.error(err))

