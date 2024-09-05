## The Python OJAI Client for MapR-DB


1. Use python 3.11
2. Create a new virtual env
3. `pip install -r build_req.txt`
4. `python -m grpc_tools.protoc -Imapr/ojai/proto --python_out=mapr/ojai/proto/gen/ --grpc_python_out=mapr/ojai/proto/gen/ mapr/ojai/proto/maprdb-server.proto`
5. Change `import maprdb_server_pb2 as maprdb__server__pb2` to `import mapr.ojai.proto.gen.maprdb_server_pb2 as maprdb__server__pb2` in `maprdb_server_pb2_grpc.py` 
6. `python setup.py bdist_wheel`

The dependencies are locked to match the apache airflow constraint file here: https://raw.githubusercontent.com/apache/airflow/constraints-2.10.0/constraints-3.11.txt

If for example a new protobuf version is wanted, update `build_req.txt` and do the above again.
