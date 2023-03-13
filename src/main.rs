use std::collections::HashMap;
use std::fs::File;
use std::io::prelude::*;
use std::ops::Range;
use std::path::Path;
use std::sync::Arc;
use std::thread::{self, JoinHandle};

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




fn scc_driver() {
   
    let (gr , gr_rev) = load_graphs(Path::new("./src/graphs/edges_small.txt"), 9) ;
    println!("{:?} \n {:?}" ,gr,gr_rev);
    let scc  = find_scc(gr, gr_rev) ;

    println!("{:?}", scc);

}


fn two_sum(seen : &mut HashMap<i64,bool>  , nums: &Vec<i64> , target : i64) -> bool {
   
    let mut found = false ;

    //
    // fn add_to_seen(x : i64 , map : &mut HashMap<i64,bool> ) {
    //    
    //     let seen  = map.get_mut(&x) ;
    //     
    //     match  seen  {
    //         Some(_) => { } ,
    //         None =>  {map.insert(x,true);} ,
    //     }
    // }
    //

    for &x in nums.iter() {
        
        let y = target - x ;
        seen.insert(x, true) ;
         
        match  seen.get(&y) {
            Some(_) =>  { 
                found = true ;
                break;
            }
            
            None => {}
        }
    
    }

    found
}

fn solution(nums : &Vec<i64> , range : Range<i64>) -> i64 {
    // let arr = vec![1,2,34,4,6,8,0] ;
    // let c = two_sum(&arnums8) ; 

    // println!("count : {}",c);
    let mut total_count = 0 ;

    let mut seen : HashMap<i64,bool>  = HashMap::new() ;
    
    for t in range {
         match  two_sum(&mut seen , &nums, t)  {
            true => {total_count += 1;} ,
            false => {}
         }
          
         println!("done , {}, count {}",t ,total_count);
         
    }

    // println!("total count {}",total_count)

    total_count
}


fn count_t() -> i64 {
    
    
    let mut file = File::open("./src/datastructures/twoSum.testcase").unwrap() ; 
    // Read the file contents into a string, returns `io::Result<usize>`
    let mut s = String::new();
    file.read_to_string(&mut s).unwrap();
    let nums_ : Vec<i64> = s.split_whitespace().map(|s| s.parse::<i64>().unwrap() ).collect() ;
    // let nums_ = vec![-3,-1,1,2,9,11,7,6,2];
 
    let nums = Arc::new(nums_) ;

    let start = -10000 ;
    let end = 10001 ;

    let cores = 4 ;

    let chunk_size = (end - start ) / cores ;
    

    let chunks = (0..cores)
        .map(|i| {
            let chunk_start = start + i * chunk_size;
            if i == cores-1 {
                return (chunk_start,end)
            }
            let chunk_end = chunk_start + chunk_size;
            (chunk_start, chunk_end)
        }) ;
    

    let mut handles : Vec<JoinHandle<i64> >= Vec::new(); 
    
    for (chunk_start, chunk_end) in chunks {
        let nums = nums.clone() ; 
        let handle = thread::spawn(move ||{
            let s = solution(&nums, chunk_start..chunk_end);
            println!("done {} {} {}",chunk_start,chunk_end,s);
            s
        }) ;
        handles.push(handle)
    }
    
    
    handles.into_iter().map(|h| h.join().unwrap()).sum()

}


fn main()  {
  let s = count_t() ;
  println!("solution {}",s)
}

