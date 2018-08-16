$(function () {
<<<<<<< HEAD
    $.get('list/').done(function (data) {
=======
    $.get(base_url + '/mentor/list/').done(function (data) {
>>>>>>> upstream/master
        var mentors = $('.people');

        data.mentors.forEach(function (mentor) {
            $('#spinner').hide();
            console.log(mentor);
            mentors.append(`
                <div>
<<<<<<< HEAD
                    <img class="" src='${mentor.profile_pic}' alt="">
=======
                    <img class="" src='/${mentor.profile_pic}' alt="">
>>>>>>> upstream/master
                        <div class="">
                        <h3>${mentor.name}</h3>
                        <h4>${mentor.detail}</h4>
                    </div>
                </div>
            `)
        })
    })
})
