$(".select_produit").change(calcul_produit);

function calcul_produit(){
let prix_ht=parseFloat($(this).val());
let tva=parseFloat($(this).parent().parent().find(".tva").val());
let prix_ttc=(prix_ht*tva/100)+prix_ht;  
$(this).parent().parent().find(".ht").val(prix_ht);
$(this).parent().parent().find(".ttc").val(prix_ttc);
calcul_total();
}

$("#bt_add").click(add_produit);

function add_produit(){
    let ligne_produit=$("tbody tr").first().clone(true);
    $("tbody").prepend(ligne_produit);
    $(".ht").first().val("");
    $(".ttc").first().val("");
}

$(".bt_del").click(del_produit);

function del_produit(){
    if ($("tbody tr").length>1) {
        $(this).parent().parent().remove();
        calcul_total();
    }
}

function calcul_total(){
    let total_ht=0;
    $(".ht").each(function(){
        total_ht=total_ht+parseFloat($(this).val());
    });
    $("#total_ht").val(total_ht);
    let total_ttc=0;
    $(".ttc").each(function(){
        total_ttc=total_ttc+parseFloat($(this).val());
    });
    $("#total_ttc").val(total_ttc);
}
$(".tva").keyup(calcul_ttc);
function calcul_ttc(){
    let tva=$(this).val();
    let prix_ht=parseFloat($(this).parent().parent().find(".ht").val());
    let prix_ttc=parseFloat((prix_ht*tva)/100+prix_ht);
    $(this).parent().parent().find(".ttc").val(prix_ttc);
    calcul_total();
}





