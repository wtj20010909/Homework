$	??K?????w?D?I????l??????!??H?}??	?6?>?I@??W?YT#@!rĚNl?5@"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$??H?}???4?8EG??As??A??Y@a??+??"^
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails??JY?8??????MbP?AQ?|a2??"^
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails????<,???5?;Nё?AHP?s?b?"^
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails?l??????/n????A??H?}M?"^
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails0*??D??^K?=???A??_?Le?*	3333??(A2g
0Iterator::Model::Prefetch::FlatMap[0]::Generator&S?!?@!s??{??X@)&S?!?@1s??{??X@:Preprocessing2F
Iterator::Model?A?f???!?k?S???)333333??1"x????:Preprocessing2P
Iterator::Model::Prefetch??ׁsF??!???O?)T?)??ׁsF??1???O?)T?:Preprocessing2Y
"Iterator::Model::Prefetch::FlatMapu?!?@!???Ո?X@)	?^)?p?1??V?c?@?:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
host?Your program is HIGHLY input-bound because 20.5% of the total step time sampled is waiting for input. Therefore, you should first focus on reducing the input time.no*high2t29.0 % of the total step time sampled is spent on 'All Others' time. This could be due to Python execution overhead.9]?%?}4@>Look at Section 3 for the breakdown of input time on the host.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
$	?*??<???	?Q?}???????MbP?!?4?8EG??	!       "	!       *	!       2$	R?Hm???c??Th????H?}M?!s??A??:	!       B	!       J	 ?M??????_?????!@a??+??R	!       Z	 ?M??????_?????!@a??+??JCPU_ONLYY]?%?}4@b 