var tinyMCELinkList = new Array(
    {% for entry in entry_list %}
    ["{{ entry.title }}", "{{ entry.get_absolute_url }}"]{% if not forloop.last %},{% endif %}
    {% endfor %}
);
