function {{ view_model_name|safe }}(){
    var self = this;
    self.{{ verbose_name_plural|safe|lower }} = ko.observableArray([]);
}