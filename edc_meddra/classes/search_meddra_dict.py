from .meddra_api_connect import MedDRAAPIConnect


class SearchMedDRADict(object):

    def __init__(self, version=None):
        self.version = version

    def _call_api(self, payload={}):
        medr = MedDRAAPIConnect()
        return medr.connect_to_meddra_dict(endpoint='search', payload=payload)

    def _basepl(self, bview='SOC', language='English', rsview='release'):
        """ Return a dictionary of base parameter for the search endpoint which
            can be used as is or added to for payload.
        """
        payload_dict = {
            'bview': bview,
            'rsview': rsview,
            'language': language,
            'stype': 1,
            'version': self.version}
        return payload_dict

    def search(self, searchterm=None, searchlogic=0, searchtype=1, addlangs=[],
               filters=[], kana=False, idiacritical=True, synonym=False,
               contains=True, soc=True, hlgt=True, hlt=True, pt=True, llt=True,
               smq=False, skip=0, take=10, separator=2):
        """ Calls search medDRA API, performs a search based on string input
            (words or MedDRA codes) and returns search results.
            @param searchterm: identified term for search
            @param searchlogic:
            @param searchtype: identifies the type of search
            @param addlangs: languages to query medDRA terms for
            @param kana: version of the Japanese language
                :note: applicable only if Japanese is selected for langs.
            @param separator: applicable for more than 2 langs selected.
            -------
            @return: medDRA search results (json)
        """

        payload = self._basepl()

        searchterm_keys = (
            searchtype,
            searchterm,
            searchlogic)

        str_searchterm_keys = (
            'searchtype',
            'searchterm',
            'searchlogic')

        searchterms_dict = {}
        for key, data in zip(str_searchterm_keys, searchterm_keys):
            searchterms_dict[key] = data
        payload['searchterms'] = [searchterms_dict]

        keys_to_add = (
            addlangs,
            filters,
            kana,
            idiacritical,
            synonym,
            contains,
            soc,
            hlgt,
            hlt,
            pt,
            llt,
            smq,
            skip,
            take,
            separator)

        str_keys = (
            'addlangs',
            'filters',
            'kana',
            'idiacritical',
            'synonym',
            'contains',
            'soc',
            'hlgt',
            'hlt',
            'pt',
            'llt',
            'smq',
            'skip',
            'take',
            'separator')

        for key, data in zip(str_keys, keys_to_add):
            payload[key] = data

        return self._call_api(payload=payload)
