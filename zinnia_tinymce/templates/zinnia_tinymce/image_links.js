var tinyMCEImageList = new Array(
    {% for file in filemodel_list %}
    ["{{ file }}", "{{ file.get_absolute_url }}"]{% if not forloop.last %},{% endif %}
    {% endfor %}
);
