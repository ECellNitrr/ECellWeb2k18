$(function () {
    $.get('https://ecellnitrr.herokuapp.com/speaker/list/').done(function (data) {
        var speakers = $('.people');

        data.speakers.forEach(function (speaker) {
            console.log(speaker);
            speakers.append(`
            <div>
                <img src='https://ecellnitrr.herokuapp.com/${speaker.profile_pic}' class="wow flipInX" alt="">
                <div class="wow fadeInUp">
                    <h3>${speaker.name}</h3>
                    <h4>${speaker.company}</h4>
                </div>
            </div>
            `)
        })
    })
})
