class OJAIList(list):
    def __init__(self):
        super(OJAIList, self).__init__()

    @staticmethod
    def set_list(value, tags=False):
        from mapr.ojai.ojai.OJAITagsBuilder import OJAITagsBuilder
        ojai_list = []
        if tags:
            dump_document = OJAITagsBuilder()
        else:
            from mapr.ojai.ojai.OJAIDocument import OJAIDocument
            dump_document = OJAIDocument()

        for elem in value:
            if isinstance(elem, list):
                if isinstance(dump_document, OJAITagsBuilder):
                    nested_list = OJAIList.set_list(elem, tags=True)
                else:
                    nested_list = OJAIList.set_list(elem)
                ojai_list.append(nested_list)
            elif isinstance(elem, dict) and bool(elem):
                tmp_dict = {}
                for k, v in elem.iteritems():
                    if isinstance(v, list):
                        tmp_dict[k] = OJAIList.set_list(v)
                    else:
                        internal_value = dump_document.set('dump', v).as_dictionary()['dump']
                        tmp_dict[k] = internal_value
                ojai_list.append(tmp_dict)
            else:
                ojai_list.append(dump_document.set('dump', elem).as_dictionary()['dump'])
            dump_document.clear()
        return ojai_list
