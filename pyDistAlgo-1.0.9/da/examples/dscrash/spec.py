# -*- generated by 1.0.9 -*-
import da
PatternExpr_198 = da.pat.TuplePattern([da.pat.ConstantPattern('Value'), da.pat.FreePattern('V2'), da.pat.FreePattern(None)])
PatternExpr_230 = da.pat.TuplePattern([da.pat.ConstantPattern('Value'), da.pat.FreePattern(None), da.pat.FreePattern(None)])
PatternExpr_255 = da.pat.TuplePattern([da.pat.ConstantPattern('Value'), da.pat.FreePattern('V2'), da.pat.FreePattern(None)])
_config_object = {}
import sys

class P(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._PSentEvent_0 = []
        self._PReceivedEvent_1 = []
        self._PReceivedEvent_2 = []
        self._events.extend([da.pat.EventPattern(da.pat.SentEvent, '_PSentEvent_0', PatternExpr_198, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_1', PatternExpr_230, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_PReceivedEvent_2', PatternExpr_255, sources=None, destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, ps, v, maxfail, **rest_354):
        super().setup(ps=ps, v=v, maxfail=maxfail, **rest_354)
        self._state.ps = ps
        self._state.v = v
        self._state.maxfail = maxfail
        self._state.V = {self._state.v}

    def run(self):
        for rnd in range(1, self._state.maxfail):

            def ExistentialOpExpr_196(v):
                for (_, _, (_ConstantPattern214_, V2, _)) in self._PSentEvent_0:
                    if (_ConstantPattern214_ == 'Value'):
                        if (self._state.v in V2):
                            return True
                return False
            self.send(('Value', {self._state.v for self._state.v in self._state.V if (not ExistentialOpExpr_196(v=self._state.v))}, self._id), to=self._state.ps)
            for attr in dir(self):
                if (attr.find('ReceivedEvent_') != (- 1)):
                    getattr(self, attr).clear()
            super()._label('_st_label_227', block=False)

            def ExistentialOpExpr_228():
                for (_, _, (_ConstantPattern245_, _, _)) in self._PReceivedEvent_1:
                    if (_ConstantPattern245_ == 'Value'):
                        if True:
                            return True
                return False
            _st_label_227 = 0
            while (_st_label_227 == 0):
                _st_label_227 += 1
                if ExistentialOpExpr_228():
                    _st_label_227 += 1
                else:
                    super()._label('_st_label_227', block=True)
                    _st_label_227 -= 1
            else:
                if (_st_label_227 != 2):
                    continue
            if (_st_label_227 != 2):
                break
            self._state.V |= {self._state.v for (_, _, (_ConstantPattern271_, V2, _)) in self._PReceivedEvent_2 if (_ConstantPattern271_ == 'Value') for self._state.v in V2}
        x = min(self._state.V)
        self.output(x)

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])

    def run(self):
        n = (int(sys.argv[1]) if (len(sys.argv) > 1) else 10)
        f = (int(sys.argv[2]) if (len(sys.argv) > 2) else 10)
        ps = self.new(P, num=n)
        for (i, p) in enumerate(list(ps)):
            self._setup({p}, (ps, i, f))
        self._start(ps)
