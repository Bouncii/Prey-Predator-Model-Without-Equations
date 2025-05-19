largeur=100;
longueur=100;
iterations=200;
job="job.sh"
simu="simu.py"


for i in 10 20
do
    mkdir predateurs_$i
    cd predateurs_$i
    for j in 100 150
    do
        mkdir proies_$j
        cd proies_$j

        for t in 3 5 6
        do
            mkdir faim_$t
            cd faim_$t

            for x in 4 7 10
            do
                mkdir nrpred_$x
                cd nrpred_$x

                for y in 4 7 10
                do
                    mkdir nrproie_$y
                    cd nrproie_$y

                    echo "$largeur" > input.txt;
                    echo "$longueur" >> input.txt;
                    echo "$iterations" >> input.txt;
                    echo "$i" >> input.txt;
                    echo "$j" >> input.txt;
                    echo "$t" >> input.txt;
                    echo "$x" >> input.txt;
                    echo "$y" >> input.txt;

                    ln -s $simu script.py
                    cp $job job.sh
                done

            done
        done

    done
done