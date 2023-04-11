class CallbackData:
    def __init__(self, class_prefix: str, *params, separator: str = ':'):
        self.separator = str(separator)
        self.class_prefix = str(class_prefix)
        self._part_names = params

    def new(self, *args, **kwargs):
        args = list(args)
        data = [self.class_prefix]

        for part in self._part_names:
            value = kwargs.pop(part, None)
            if not value:
                if args:
                    value = args.pop(0)
                else:
                    raise ValueError(f'Value for {part!r} was not passed!')
            data.append(str(value))

        callback_data = self.separator + self.separator.join(data)
        if len(callback_data.encode()) > 64:
            raise ValueError('Resulted callback data is too long!')
        return callback_data

    def filter(self, **config):
        filter_hash = dict()
        current_filter = self.class_prefix + self.separator
        for key in self._part_names:
            current_filter += str(config.get(key, '')) + self.separator
            filter_hash[key] = str(config.get(key, ''))
        current_filter = self.separator + current_filter[: len(current_filter) - 1]

        return {self.class_prefix: {current_filter: filter_hash}}
