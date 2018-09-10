


def component_factory(XBLOCKS_FACTORY, identifier):
    if XBLOCKS_FACTORY:
        for component in XBLOCKS_FACTORY['components']:
            if identifier.startswith(component["module"] + "_"):
                import ipdb; ipdb.set_trace()
                suffix = str(identifier.split("_")[2].capitalize())  # TODO: strengthen
                base_class_name = component["base_class"]
                mod = __import__(component["module"])
                BaseClass = getattr(mod, base_class_name)
                attributes = {klass["suffix"]: klass["attributes"] for klass in component["subclasses"]}[suffix]
                ComponentClass = type(base_class_name + suffix, (BaseClass,), attributes)
                return ComponentClass
    return None


def add_dynamic_components(XBLOCKS_FACTORY, advanced_component_templates, categories, create_template_dict):
    """
    """
    if XBLOCKS_FACTORY:
        for component in XBLOCKS_FACTORY['components']:
            for class_info in component["subclasses"]:
                display_name = class_info["display"]
                key = component["module"] + "_" + class_info["suffix"]
                advanced_component_templates['templates'].append(
                    create_template_dict(
                        display_name,
                        key
                        )
                )
                categories.add(key)
