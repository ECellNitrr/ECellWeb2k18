reverse = false

function insert_speaker(speakers, location, to_hide) {
    var year = 2018
    // create a div
    var div = document.createElement('div')
    div.id = year
    // div.classList.add('years', to_hide ? "d-none" : "d-block")
    // make the template
    speakers.forEach(speaker => {
        div.innerHTML += reverse?`
            <svg  class=svg-top xmlns=http://www.w3.org/2000/svg viewBox="0 0 100 10" preserveAspectRatio=none>
                <polygon points="100 0 100 10 0 10" /> </svg>
        `:''
        div.innerHTML +=
            `<div class=${reverse? 'grey':''}>
                <div class='d-md-flex speaker container ${reverse ? "reverse pb-4" : ""}'>
                    <div class='s-img text-center'>
                        <img src='${speaker.profile_pic}' class="wow flipInX my-2" alt="">
                    </div>
                    <div class='s-info d-flex align-items-center'>
                        <div class="wow fadeInUp">
                            <h4>${speaker.name} <span class='badge badge-primary'>${speakers.year}</span></h4>
                            <h5>${speaker.company}</h5>
                            <p>${speaker.description}</p>
                            <div class='text-center text-md-left'>
                                <a href='${speaker.social_media}' class='btn btn-outline-danger btn-sm'><i class='fa fa-anchor'></i><strong> follow</strong></a>
                            </div>
                        </div>
                    </div>
            </div></div>`
        div.innerHTML +=reverse?`
            <svg class=svg-bottom xmlns=http://www.w3.org/2000/svg viewBox="0 0 100 10" preserveAspectRatio=none>
                <polygon points="100 0 100 10 0 10" /> </svg>
        `:''

        reverse = !reverse
    })

    location.append(div)
}

$(function () {
    $.get(base_url + '/speakers/list/').done(function (data) {
        console.log(data)
        $('#spinner').hide()
        var speakers_div = $('.people');

        var k18 = data.speakers.filter(speaker => speaker.year == 2018)
        var k17 = data.speakers.filter(speaker => speaker.year == 2017)
        var k16 = data.speakers.filter(speaker => speaker.year == 2016)
        var k15 = data.speakers.filter(speaker => speaker.year == 2015)

        insert_speaker(k18, speakers_div, false)
        insert_speaker(k17, speakers_div, true)
        insert_speaker(k16, speakers_div, true)
        insert_speaker(k15, speakers_div, true)

    })
})

// load more button handler

$('#load_more_btn').on('click', function() {
    document.querySelector('.d-none').classList.remove('d-none')
    if(!document.querySelector('.d-none')){
        $(this).hide()
    }
})