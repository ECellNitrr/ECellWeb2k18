$(function () {
    $.get('https://ecellnitrr.herokuapp.com/mentor/list/').done(function (data) {
        var mentors = $('.people');

        data.mentors.forEach(function (mentor) {
            console.log(mentor);
            mentors.append(`
                <div>
                    <img data-wow-delay=.2s class="wow flipInX" src='https://ecellnitrr.herokuapp.com/${mentor.profile_pic}' alt="">
                        <div class="wow fadeInDown">
                        <h3>${mentor.name}</h3>
                        <h4>${mentor.detail}</h4>
                    </div>
                </div>
            `)
        })
    })
})
