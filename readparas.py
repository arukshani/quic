import pandas as pd
import json

def read_paras():
    # df = pd.read_json('./example-del.json')
    # print(df[0])
    with open('safari_google.json') as f:
        data = json.load(f)
    # print("---Chrome cloudflare---")
    print("initial_max_stream_data_uni: ", data['tls.quic.parameter.initial_max_stream_data_uni'])
    print("max_datagram_frame_size: ",data['tls.quic.parameter.max_datagram_frame_size'])
    print("initial_source_connection_id: ", data['tls.quic.parameter.initial_source_connection_id'])
    print("initial_max_streams_uni: ",data['tls.quic.parameter.initial_max_streams_uni'])
    # print(data['tls.quic.parameter.grease_quic_bit'])
    print("initial_max_stream_data_bidi_local: ", data['tls.quic.parameter.initial_max_stream_data_bidi_local'])
    # print(data['tls.quic.parameter.GREASE'])
    print("initial_max_data: ",data['tls.quic.parameter.initial_max_data'])
    # print("active_connection_id_limit: ", data['tls.quic.parameter.active_connection_id_limit'])
    print("initial_max_stream_data_bidi_remote: ",data['tls.quic.parameter.initial_max_stream_data_bidi_remote'])
    # print(data['tls.quic.parameter.disable_active_migration'])
    print("max_idle_timeout: ", data['tls.quic.parameter.max_idle_timeout'])
    print("initial_max_streams_bidi: ", data['tls.quic.parameter.initial_max_streams_bidi'])

read_paras()