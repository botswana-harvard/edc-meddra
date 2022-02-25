from .meddra_api_connect import MedDRAAPIConnect


class DetailsMedDRADict(object):

    def __init__(self, version=None):
        self.version = version

    def _call_api(self, payload={}):
        medr = MedDRAAPIConnect()
        return medr.connect_to_meddra_dict(endpoint='detail', payload=payload)

    def _basepl(self, bview='SOC', language='English', rsview='release'):
        """ Return a dictionary of base parameter for the detail endpoint which
            can be used as is or added to for payload.
        """
        payload_dict = {
            'bview': bview,
            'rsview': rsview,
            'lang': language,
            'rtype': 'M',
            'ver': self.version}
        return payload_dict

    def details(self, code=None, term_type='LLT', addlangs=[], kana=False,
                separator=2):
        """ Calls detail medDRA API, provide the details for a specific code or
            term.
            @param term code: medDRA code assigned to a term
            @param term_type:
            @param addlangs: languages to query medDRA terms for
            @param kana: version of the Japanese language
                :note: applicable only if Japanese is selected for langs.
            @param separator: applicable for more than 2 langs selected.
            -------
            @return: medDRA details response (json)
        """
        payload = self._basepl()

        keys_to_add = (
            code,
            term_type,
            addlangs,
            kana,
            separator)

        str_keys = (
            'code',
            'type',
            'addlangs',
            'kana',
            'separator')

        for key, data in zip(str_keys, keys_to_add):
            payload[key] = data
        payload.update(
            {'pcode': 0,
             'syncode': 0,
             'lltcode': 0,
             'ptcode': 0,
             'hltcode': 0,
             'hlgtcode': 0,
             'soccode': 0,
             'smqcode': 0, })

        return self._call_api(payload=payload)
