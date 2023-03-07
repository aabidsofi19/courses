use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

type Graph = Vec<Vec<usize>> ;

#[derive(Clone,Copy,PartialEq, Eq)]
enum Pass {
    Ordering , 
    Sccs
}


fn load_graphs(file_path : &Path , n : usize ) -> (Graph,Graph){

    let mut file = File::open(file_path).unwrap() ; 

    // Read the file contents into a string, returns `io::Result<usize>`
    let mut s = String::new();
    file.read_to_string(&mut s).unwrap();

    let lines = s.split("\n");
    let mut gr : Graph = vec![vec![] ; n ] ;
    let mut gr_rev : Graph = vec![vec![] ; n] ;
    
    for line in lines {
        if line == " " || line == "" {
            continue;
        } 
        println!("line {}",line);
        let mut x = line.split(" ") ;
        let u : usize = x.next().unwrap().parse::<usize>().unwrap() ; 
        let v : usize = x.next().unwrap().parse::<usize>().unwrap() ;

        gr[u].push(v) ;
        gr_rev[v].push(u) ;

    } 



    (gr,gr_rev)

}

fn find_scc(gr : Graph , gr_rev : Graph ) -> Vec<usize> {
    
    let n  =  gr.len() ;
    
    fn search(graph : &Graph , s : usize , pass : Pass , visited: &mut Vec<bool> , ordering: &mut Vec<usize> , finish_time : &mut usize , scc : &mut Vec<usize> , leader : usize) {
        println!("searc"); 
        visited[s] = true ;
        
        if pass == Pass::Sccs {

           scc[leader] = scc[leader] + 1 
        }

        for &v in graph[s].iter() {
            if ! visited[v] {
                search(graph, v, pass, visited, ordering,finish_time, scc,leader)
            }
        }

        if pass == Pass::Ordering {
            *finish_time += 1;
            println!("finished {} in {}",s , finish_time);
            ordering[*finish_time] = s; 
        }
    }


    // Set the ordering 
    // let mut stack = vec![] ;
    let mut visited = vec![false ; n] ; 
    let mut ordering : Vec<usize> = vec![0 ; n].try_into().unwrap() ;
    let mut finish_time : usize = 0 ;

    for v in  (1..n).rev() {
        if ! visited[v] {
            search(&gr_rev , v , Pass::Ordering,  &mut visited , &mut ordering , &mut finish_time , &mut vec![0], 0) ;    

        }
    }    

    
    // Find the Sccs 
    let mut visited = vec![false ; n] ; 
    let mut scc =     vec![0 ; n] ;
    let mut leader : usize ; 
    for &v in  ordering.iter().rev() {
        if ! visited[v] {
            leader = v; 
            search(&gr , v , Pass::Sccs , &mut visited ,&mut vec![], &mut 0 , &mut scc , leader ) ;    
        }
    }    

    scc.sort() ;
    scc.reverse() ;

    return scc

}




fn main() {
   
    let (gr , gr_rev) = load_graphs(Path::new("./src/graphs/edges_small.txt"), 9) ;
    println!("{:?} \n {:?}" ,gr,gr_rev);
    let scc  = find_scc(gr, gr_rev) ;

    println!("{:?}", scc);

}
