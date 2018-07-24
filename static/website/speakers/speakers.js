function insert_speaker(speakers, location) {
    var year = speakers[0].year
    // create a div
    var div = document.createElement('div')
    div.id = year
    div.innerHTML += `<h3>${year}</h3>`

    speakers.forEach(speaker => {
        div.innerHTML += 
            `<div>
                <img src='/${speaker.profile_pic}' class="wow flipInX" alt="">
                <div class="wow fadeInUp">
                    <h3>${speaker.name}</h3>
                    <h4>${speaker.company}</h4>
                    <p>${speaker.description}</p>
                </div>
            </div>`
    })

    // append div to the dom
    location.append(div)
}

$(function () {
    $.get('https://ecellnitrr.herokuapp.com/speaker/list/').done(function (data) {
        var speakers_div = $('.people');

        var k15 = data.speakers.filter(speaker => speaker.year == 2015)
        var k16 = data.speakers.filter(speaker => speaker.year == 2016)
        var k17 = data.speakers.filter(speaker => speaker.year == 2017)
        var k18 = data.speakers.filter(speaker => speaker.year == 2018)

        insert_speaker(k15, speakers_div)
        insert_speaker(k16, speakers_div)
        insert_speaker(k17, speakers_div)
        insert_speaker(k18, speakers_div)
    })
})
