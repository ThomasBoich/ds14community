class CustomUserRouter:
    route_app_labels = {'users'}  # замените 'myapp' на имя вашего приложения

    def db_for_read(self, model, **hints):
        if model._meta.model_name == 'customuser':
            return 'users'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.model_name == 'customuser':
            return 'users'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.model_name == 'customuser' or obj2._meta.model_name == 'customuser':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if model_name == 'customuser':
            return db == 'users'
        return None