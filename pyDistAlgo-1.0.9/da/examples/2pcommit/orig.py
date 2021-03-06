# -*- generated by 1.0.9 -*-
import da
PatternExpr_187 = da.pat.TuplePattern([da.pat.ConstantPattern('vote'), da.pat.FreePattern(None)])
PatternExpr_193 = da.pat.BoundPattern('_BoundPattern194_')
PatternExpr_217 = da.pat.TuplePattern([da.pat.ConstantPattern('vote'), da.pat.ConstantPattern('aborting')])
PatternExpr_224 = da.pat.BoundPattern('_BoundPattern225_')
PatternExpr_245 = da.pat.TuplePattern([da.pat.ConstantPattern('vote'), da.pat.ConstantPattern('ready')])
PatternExpr_252 = da.pat.FreePattern('c')
PatternExpr_285 = da.pat.TuplePattern([da.pat.ConstantPattern('vote'), da.pat.ConstantPattern('ready')])
PatternExpr_292 = da.pat.BoundPattern('_BoundPattern293_')
PatternExpr_318 = da.pat.ConstantPattern('done')
PatternExpr_322 = da.pat.BoundPattern('_BoundPattern323_')
PatternExpr_226 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern232_')]), da.pat.TuplePattern([da.pat.ConstantPattern('vote'), da.pat.ConstantPattern('aborting')])])
PatternExpr_294 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern300_')]), da.pat.TuplePattern([da.pat.ConstantPattern('vote'), da.pat.ConstantPattern('ready')])])
PatternExpr_324 = da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.TuplePattern([da.pat.FreePattern(None), da.pat.FreePattern(None), da.pat.BoundPattern('_BoundPattern330_')]), da.pat.ConstantPattern('done')])
PatternExpr_372 = da.pat.ConstantPattern('prepare')
PatternExpr_376 = da.pat.FreePattern('coord')
PatternExpr_402 = da.pat.ConstantPattern('abort')
PatternExpr_411 = da.pat.ConstantPattern('commit')
PatternExpr_415 = da.pat.FreePattern('coord')
_config_object = {}
import sys
from random import randint

class Coordinator(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._CoordinatorReceivedEvent_0 = []
        self._CoordinatorReceivedEvent_1 = []
        self._CoordinatorReceivedEvent_2 = []
        self._CoordinatorReceivedEvent_3 = []
        self._CoordinatorReceivedEvent_4 = []
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_CoordinatorReceivedEvent_0', PatternExpr_187, sources=[PatternExpr_193], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_CoordinatorReceivedEvent_1', PatternExpr_217, sources=[PatternExpr_224], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_CoordinatorReceivedEvent_2', PatternExpr_245, sources=[PatternExpr_252], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_CoordinatorReceivedEvent_3', PatternExpr_285, sources=[PatternExpr_292], destinations=None, timestamps=None, record_history=True, handlers=[]), da.pat.EventPattern(da.pat.ReceivedEvent, '_CoordinatorReceivedEvent_4', PatternExpr_318, sources=[PatternExpr_322], destinations=None, timestamps=None, record_history=True, handlers=[])])

    def setup(self, cohorts, **rest_514):
        super().setup(cohorts=cohorts, **rest_514)
        self._state.cohorts = cohorts
        pass

    def run(self):
        self.to_commit()
        self.output('terminating')

    def to_commit(self):
        self.send('prepare', to=self._state.cohorts)
        super()._label('_st_label_178', block=False)
        c = None

        def UniversalOpExpr_179():
            nonlocal c
            for c in self._state.cohorts:

                def ExistentialOpExpr_185(c):
                    for (_, (_, _, _BoundPattern201_), (_ConstantPattern203_, _)) in self._CoordinatorReceivedEvent_0:
                        if (_BoundPattern201_ == c):
                            if (_ConstantPattern203_ == 'vote'):
                                if True:
                                    return True
                    return False
                if (not ExistentialOpExpr_185(c=c)):
                    return False
            return True
        _st_label_178 = 0
        while (_st_label_178 == 0):
            _st_label_178 += 1
            if UniversalOpExpr_179():
                _st_label_178 += 1
            else:
                super()._label('_st_label_178', block=True)
                _st_label_178 -= 1
        c = None

        def ExistentialOpExpr_210():
            nonlocal c
            for c in self._state.cohorts:
                if PatternExpr_226.match_iter(self._CoordinatorReceivedEvent_1, _BoundPattern232_=c, SELF_ID=self._id):
                    return True
            return False
        if ExistentialOpExpr_210():
            s = {c for c in self._state.cohorts for (_, (_, _, _FreePattern260_), (_ConstantPattern262_, _ConstantPattern264_)) in self._CoordinatorReceivedEvent_2 if (_FreePattern260_ == c) if (_ConstantPattern262_ == 'vote') if (_ConstantPattern264_ == 'ready')}
            self.send('abort', to=s)
            self.abort()
        c = None

        def UniversalOpExpr_278():
            nonlocal c
            for c in self._state.cohorts:
                if (not PatternExpr_294.match_iter(self._CoordinatorReceivedEvent_3, _BoundPattern300_=c, SELF_ID=self._id)):
                    return False
            return True
        if UniversalOpExpr_278():
            self.send('commit', to=self._state.cohorts)
            super()._label('_st_label_310', block=False)
            c = None

            def UniversalOpExpr_311():
                nonlocal c
                for c in self._state.cohorts:
                    if (not PatternExpr_324.match_iter(self._CoordinatorReceivedEvent_4, _BoundPattern330_=c, SELF_ID=self._id)):
                        return False
                return True
            _st_label_310 = 0
            while (_st_label_310 == 0):
                _st_label_310 += 1
                if UniversalOpExpr_311():
                    _st_label_310 += 1
                else:
                    super()._label('_st_label_310', block=True)
                    _st_label_310 -= 1
            self.commit()

    def abort(self):
        self.output('abort')

    def commit(self):
        self.output('commit')

class Cohort(da.DistProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([da.pat.EventPattern(da.pat.ReceivedEvent, '_CohortReceivedEvent_0', PatternExpr_372, sources=[PatternExpr_376], destinations=None, timestamps=None, record_history=None, handlers=[self._Cohort_handler_371]), da.pat.EventPattern(da.pat.ReceivedEvent, '_CohortReceivedEvent_1', PatternExpr_402, sources=None, destinations=None, timestamps=None, record_history=None, handlers=[self._Cohort_handler_401]), da.pat.EventPattern(da.pat.ReceivedEvent, '_CohortReceivedEvent_2', PatternExpr_411, sources=[PatternExpr_415], destinations=None, timestamps=None, record_history=None, handlers=[self._Cohort_handler_410])])

    def setup(self, failure_rate, **rest_514):
        super().setup(failure_rate=failure_rate, **rest_514)
        self._state.failure_rate = failure_rate
        self._state.terminate = False

    def run(self):
        super()._label('_st_label_454', block=False)
        _st_label_454 = 0
        while (_st_label_454 == 0):
            _st_label_454 += 1
            if self._state.terminate:
                _st_label_454 += 1
            else:
                super()._label('_st_label_454', block=True)
                _st_label_454 -= 1

    def prepared(self):
        return (randint(0, 100) > self._state.failure_rate)

    def ready(self):
        self.output('ready')

    def abort(self):
        self.output('abort')
        self._state.terminate = True

    def commit(self):
        self.output('commit')
        self._state.terminate = True

    def _Cohort_handler_371(self, coord):
        if self.prepared():
            self.send(('vote', 'ready'), to=coord)
            self.ready()
        else:
            self.send(('vote', 'aborting'), to=coord)
            self.abort()
    _Cohort_handler_371._labels = None
    _Cohort_handler_371._notlabels = None

    def _Cohort_handler_401(self):
        self.abort()
    _Cohort_handler_401._labels = None
    _Cohort_handler_401._notlabels = None

    def _Cohort_handler_410(self, coord):
        self.send('done', to=coord)
        self.commit()
    _Cohort_handler_410._labels = None
    _Cohort_handler_410._notlabels = None

class Node_(da.NodeProcess):

    def __init__(self, procimpl, props):
        super().__init__(procimpl, props)
        self._events.extend([])

    def run(self):
        ncohorts = (int(sys.argv[1]) if (len(sys.argv) > 1) else 10)
        fail_rate = (int(sys.argv[2]) if (len(sys.argv) > 2) else 10)
        cohorts = self.new(Cohort, (fail_rate,), num=ncohorts)
        coordinators = self.new(Coordinator, (cohorts,), num=1)
        self._start((cohorts | coordinators))
