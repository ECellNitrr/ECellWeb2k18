function add_member(target, members) {
    members.forEach(function (member) {
        var member_html = `
            <div class="member">
                <img src="https://ecellnitrr.herokuapp.com/${member.url}">
                <div class="description">
                    <h4 class="name">${member.name}</h4>
                </div>
            </div>
        `
        target.append(member_html)
    })
}

$(function () {

    var director = $('#director')
    var overall_co = $('#overall-co')
    var head_co = $('#head-co')
    var managers = $('#managers')
    var executives = $('#executives')
    var head_career_dev = $('#head_career-dev')
    var faculty_incharge = $('#faculty_incharge')

    $.get('https://ecellnitrr.herokuapp.com/team/list').then(function (data) {
        console.log(JSON.stringify(data, null, 2));
        add_member(director, data['Director, NIT Raipur'])
        add_member(head_career_dev, data['Head of Career development'])
        add_member(faculty_incharge, data['Faculty Incharge'])
        add_member(head_co, data['Head Co-ordinator'])
        add_member(overall_co, data['Overall Co-ordinator'])
        add_member(managers, data['manager'])
        add_member(executives, data['executive'])
    })

})