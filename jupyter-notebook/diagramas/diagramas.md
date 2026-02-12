# Diagramas

https://diagrams.mingrammer.com/docs/getting-started/examples

Instalação:

https://diagrams.mingrammer.com/docs/getting-started/installation

Exemplo:

```bash
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB

with Diagram("Grouped Workers", show=False, direction="TB"):
    ELB("lb") >> [EC2("worker1"),
                  EC2("worker2"),
                  EC2("worker3"),
                  EC2("worker4"),
                  EC2("worker5")] >> RDS("events")
    
print("Arquivo criado com sucesso !!!")

```

Um arquivo `grouped_workers.png` será criado:

<p align="center">
<img src="grouped_workers.png">
</p>