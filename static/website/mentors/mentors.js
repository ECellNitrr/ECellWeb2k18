$(function () {
    $.get(base_url + '/mentor/list/').done(function (data) {
        var mentors = $('.people');
        console.log(data)
        $('#spinner').hide();
        
        data.mentors.forEach(function (mentor) {
            console.log(mentor);
            mentors.append(`
                <div>
                    <img class="" src='/${mentor.profile_pic}' alt="">
                        <div class="">
                        <h3>${mentor.name}</h3>
                        <h4>${mentor.detail}</h4>
                    </div>
                </div>
            `)
        })
    })
})
