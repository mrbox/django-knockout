
function {{ model_name }}Model(data) {
    var self = this;
    {% for field in fields %}self.{{ field.name|safe }} = data.{{ field.name|safe }};
    {% endfor %}
}