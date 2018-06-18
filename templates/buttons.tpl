        <p><div class="is-centered">
        		%if previous != 15784:
               		<a href="/{{link}}/{{previous}}" class="button is-rounded"><i class="fas fa-angle-left"></i></a>
                %end
                %if today:
                    <a href="/{{link}}/{{today}}" class="button is-rounded">today</a>
                %end
                <a href="/{{link}}/{{next}}" class="button is-selected is-rounded"><i class="fas fa-angle-right"></i></a>
            </div></p>