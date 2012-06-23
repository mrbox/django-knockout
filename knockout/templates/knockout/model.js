
function {{ model_name }}(data) {
    var self = this;
    {% for field in fields %}self.{{ field.name|safe }} = ko.observable(data.{{ field.name|safe }});
    {% endfor %}
}