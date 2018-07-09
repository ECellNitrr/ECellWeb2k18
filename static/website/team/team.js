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
    var dean_student_welfare = $('#dean_student_welfare')
    var dean_research = $('#dean_research')
    var faculty_incharge = $('#faculty_incharge')

    console.log(dean_student_welfare,dean_research,faculty_incharge);

    $.get('https://ecellnitrr.herokuapp.com/team/list').then(function (data) {
        add_member(director, data['Director, NIT Raipur'])
        add_member(dean_student_welfare, data['Dean Student Welfare'])
        add_member(dean_research, data['Dean Research & Cons.'])
        add_member(faculty_incharge, data['Faculty Incharge'])
        add_member(head_co, data['Head Co-ordinator'])
        add_member(overall_co, data['Overall Co-ordinator'])
        add_member(managers, data['manager'])
        add_member(executives, data['executive'])
    })

})