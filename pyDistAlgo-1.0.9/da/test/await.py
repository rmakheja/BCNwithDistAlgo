# -*- generated by 1.0.9 -*-
import da
PatternExpr_174 = da.pat.TuplePattern([da.pat.ConstantPattern('Y')])
PatternExpr_184 = da.pat.TuplePattern([da.pat.ConstantPattern('Z')])
_config_object = {}

class P(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_0', PatternExpr_174, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_173]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_1', PatternExpr_184, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._P_handler_183])])

    def setup(self, **rest_289):
        super().setup(**rest_289)
        self._state.d = 1
        self._state.x = 1

    def run(self):
        super()._label('l', block=False)
        _st_label_194 = 0
        while True:
            if (_st_label_194 == 2):
                break
            elif (_st_label_194 == 1):
                super()._label('l', block=True)
            _st_label_194 = 1
            if (self._state.d == 1):
                self.output('d is 1.')
            elif (self._state.x == 1):
                self.output('x is 1.')
            else:
                self.output('neither d nor x is 1.')
                _st_label_194 += 1

    def _P_handler_173(self):
        self._state.d = 0
    _P_handler_173._labels = None
    _P_handler_173._notlabels = None

    def _P_handler_183(self):
        self._state.x = 0
    _P_handler_183._labels = None
    _P_handler_183._notlabels = None

class Q(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])

    def setup(self, ps, **rest_289):
        super().setup(ps=ps, **rest_289)
        self._state.ps = ps
        pass

    def run(self):
        self.output("Sending 'X'.")
        self.send(('X',), to=self._state.ps)
        super()._label('_st_label_227', block=False)
        _st_label_227 = 0
        self._timer_start()
        while (_st_label_227 == 0):
            _st_label_227 += 1
            if False:
                _st_label_227 += 1
            elif self._timer_expired:
                _st_label_227 += 1
            else:
                super()._label('_st_label_227', block=True, timeout=2)
                _st_label_227 -= 1
        self.output("Sending 'X'.")
        self.send(('X',), to=self._state.ps)
        super()._label('_st_label_238', block=False)
        _st_label_238 = 0
        self._timer_start()
        while (_st_label_238 == 0):
            _st_label_238 += 1
            if False:
                _st_label_238 += 1
            elif self._timer_expired:
                _st_label_238 += 1
            else:
                super()._label('_st_label_238', block=True, timeout=2)
                _st_label_238 -= 1
        self.output("Sending 'Y'.")
        self.send(('Y',), to=self._state.ps)
        super()._label('_st_label_249', block=False)
        _st_label_249 = 0
        self._timer_start()
        while (_st_label_249 == 0):
            _st_label_249 += 1
            if False:
                _st_label_249 += 1
            elif self._timer_expired:
                _st_label_249 += 1
            else:
                super()._label('_st_label_249', block=True, timeout=2)
                _st_label_249 -= 1
        self.output("Sending 'Z'.")
        self.send(('Z',), to=self._state.ps)
        while False:
            self.output('Fail!')

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])

    def run(self):
        ps = self.new(P, [], 1)
        qs = self.new(Q, [ps], 1)
        self._start(ps)
        self._start(qs)
