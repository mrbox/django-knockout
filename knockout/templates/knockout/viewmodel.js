function {{ model_name|safe }}ListViewName(){
    var self = this;
    self.{{ verbose_name_plural|safe|lower }} = ko.observableArray([]);
}