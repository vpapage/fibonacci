# fibonacci
This is a dummy project using flask and an python app calculating fibonacci series


<!-- .gitconfig

[user]
    email = vaspapts@intracom-telecom.com
    name = vasiliki papageorgiou
[url "https://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:x-oauth-basic@github.com/"]
    insteadOf = https://github.com/ 
    
-->

## TODO 
    python fibonacci.py
    GO TO: 127.0.0.1:5000

    docker build -t vaspapts/fibonacci:new-flask .
    docker login
    docker push vaspapts/fibonacci:new-flask
    docker build -t vaspapts/fibonacci:new-flask .

    # run a Docker container using the created Docker image
    docker run -p 5000:5000 vaspapts/fibonacci:new-flask

    # DEPLOY
    kubectl apply -f deployment.yaml
    kubectl get deployment
    kubectl get svc
    kubectl service fib-service  # Μελετάς το svc
    kubectl apply -f ingress.yaml
    kubectl get ingress

    # Set up DNS or hosts file
    <Ingress-IP>  my-flask-app.example.com