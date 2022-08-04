COUNTER=$(head -n 1 counter.txt)
((COUNTER++))

DOCKERIMG="manojjahgirdar/ddc-argocd-demo"
DOCKERTAG="v$COUNTER"

echo $COUNTER > counter.txt

echo "[1/3]: Building docker image $DOCKERIMG:$DOCKERTAG"

docker build -t $DOCKERIMG:$DOCKERTAG . && docker push $DOCKERIMG:$DOCKERTAG

echo "[2/3]: Patching deploy.yaml file"

kubectl patch --local -f ../scripts/deploy.yaml -p \
'{"spec":{"template":{"spec":{"containers":[{"name":"ddc-argocd-demo","image":"'$DOCKERIMG:$DOCKERTAG'"}]}}}}' \
-o yaml &> ../scripts/deployment.yaml && mv ../scripts/deployment.yaml ../scripts/deploy.yaml

echo "[3/3]: Pushing to GitHub"

cd ../ && git add . && git commit -m "Deployment of image $DOCKERIMG:$DOCKERTAG" && git push

