from UI import dashboard
from multiprocessing import Process, Value
import simulate_webserver
import simulate_cpu

p1 = Process(target=simulate_webserver.random_logs)
p1.start()
graph_type = Value('i',0)
p2 = Process(target=dashboard.render_dashboard,args=(graph_type,))
p2.start()
p3 = Process(target=simulate_cpu.generate_graph, args=(graph_type,))
p3.start()