def qs2html(qs_list):
    s = '<table>'
    for record in qs_list:
        s += f'<tr><td>{record.first_name}</td>\
        <td>{record.last_name}</td>\
        <td>{record.email}</td>\
        <td><a href="update/{record.pk}">Edit</a></td>\
        </tr>'
    s += '</table>'
    return s
