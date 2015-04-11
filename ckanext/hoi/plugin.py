import logging
import ckan.plugins as plugins
import ckan.plugins.toolkit as tk

log = logging.getLogger(__name__)


class HoiDatasetPlugin(plugins.SingletonPlugin, tk.DefaultDatasetForm):
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.IConfigurer)

    def _modify_package_schema(self, schema):
        log.warning(schema)
        schema.update({
            'title_sv': [tk.get_validator('ignore_missing'),
                         tk.get_converter('convert_to_extras')]
        })
        return schema

    def create_package_schema(self):
        schema = super(HoiDatasetPlugin, self).create_package_schema()
        return self._modify_package_schema(schema)

    def update_package_schema(self):
        schema = super(HoiDatasetPlugin, self).update_package_schema()
        return self._modify_package_schema(schema)

    def show_package_schema(self):
        schema = super(HoiDatasetPlugin, self).show_package_schema()
        schema.update({
            'title_sv': [tk.get_converter('convert_from_extras'),
                         tk.get_validator('ignore_missing')]
        })
        log.warning(schema)
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
