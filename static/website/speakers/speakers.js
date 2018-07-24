reverse = false

function insert_speaker(speakers, location) {
    var year = speakers[0].year
    // create a div
    var div = document.createElement('div')
    div.id = year
    div.classList.add('years')
    div.innerHTML += `<h3 class='display-4 font-weight-bold'>${year}</h3><hr>`

    speakers.forEach(speaker => {
        div.innerHTML += 
            `<div class='d-flex speaker container'>
                    <div class='s-img'>
                        <img src='/${speaker.profile_pic}' class="wow flipInX" alt="">
                    </div>
                    <div class='s-info d-flex align-items-center'>
                        <div class="wow fadeInUp">
                            <h4>${speaker.name}</h4>
                            <h5>${speaker.company}</h5>
                            <p>${speaker.description}</p>
                        </div>
                    </div>
            </div>`

        reverse = !reverse 
    })

    // append div to the dom
    
    location.append(div)
}

$(function () {
    $.get('https://ecellnitrr.herokuapp.com/speaker/list/').done(function (data) {
        var speakers_div = $('.people');

        var k18 = data.speakers.filter(speaker => speaker.year == 2018)
        var k17 = data.speakers.filter(speaker => speaker.year == 2017)
        var k16 = data.speakers.filter(speaker => speaker.year == 2016)
        var k15 = data.speakers.filter(speaker => speaker.year == 2015)

        insert_speaker(k18, speakers_div)
        insert_speaker(k17, speakers_div)
        insert_speaker(k16, speakers_div)
        insert_speaker(k15, speakers_div)
    })
})
