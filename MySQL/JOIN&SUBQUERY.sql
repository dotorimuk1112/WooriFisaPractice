-- 모든 부서의 정보와 함께 커미션이 있는 직원들의 커미션과 이름을 조회해 보세요.
SELECT * FROM emp;
SELECT deptno, comm
FROM emp
WHERE comm IS NOT NULL;

-- 모든 부서의 부서별 연봉에 대한 총합과 평균과 표준편차를 구하고
-- 모든 부서의 사원수를 구해 보세요.
SELECT deptno, SUM(sal), avg(sal), stddev(sal)
FROM emp
GROUP BY deptno;


SELECT * FROM emp;
SELECT * FROM dept;
-- 각 관리자의 부하직원수와 부하직원들의 평균연봉을 구해 보세요.
SELECT deptno, COUNT(*), avg(sal)
FROM emp
WHERE job != 'MANAGER'
GROUP BY deptno;

# Sub-Query 
-- 쿼리 안쪽에 쿼리를 넣을수 있다.
-- where 절에서의 서브쿼리
-- scott과 같은 부서에 있는 직원 이름을 검색해 보세요.
SELECT e.ename, e.deptno
FROM emp e
WHERE e.deptno = (SELECT e.deptno
FROM emp e
WHERE e.ename = 'SCOTT');

-- 직무(job)가 Manager인 사람들이 속한 부서의 부서번호와 부서명 , 지역을 조회해 보세요.
	-- manager 사람들이 다수이기 때문에 where절에 in 을 활용!
SELECT deptno, dname, loc
FROM dept
WHERE deptno in (SELECT deptno
				 FROM emp
				 WHERE job = 'MANAGER');
                 
# from 절에서의 서브쿼리
-- emp 테이블에서 급여가 2000이 넘는 사람들의 이름과 부서번호, 부서이름, 지역 조회해 보세요.
SELECT e.ename, e.deptno, d.dname, d.loc, e.sal
FROM emp e, dept d
WHERE e.sal >= 2000 AND e.deptno = d.deptno;

SELECT g.ename, g.deptno, g.dname, g.loc, g.sal
FROM 
(SELECT e.ename, e.deptno, d.dname, d.loc, e.sal
FROM emp e, dept d
WHERE e.deptno = d.deptno) g
WHERE g.sal >= 2000;


-- emp 테이블에서 커미션이 있는 사람들의 이름과 부서번호, 부서이름, 지역을 조회해 보세요.
SELECT c.ename, c.comm, c.deptno, c.dname, c.loc
FROM (SELECT emp.ename, emp.comm, dept.deptno, dept.dname, dept.loc
FROM emp, dept
WHERE dept.deptno = emp.deptno) c
WHERE c.comm > 0;

SELECT emp.ename, emp.comm, dept.deptno, dept.dname, dept.loc
FROM emp, dept
WHERE dept.deptno = emp.deptno;


-- emp 테이블에서 커미션이 있는 사람들의 이름과 부서번호, 부서이름, 지역을 조회해 보세요.
-- join 절에서의 서브쿼리
SELECT c.ename, c.comm, c.deptno, c.dname, c.loc
FROM dept d inner join (SELECT emp.ename, emp.comm, dept.deptno, dept.dname, dept.loc
FROM emp, dept
WHERE dept.deptno = emp.deptno) c
ON c.comm > 0 AND d.deptno = c.deptno;



-- 모든 부서의 부서이름과, 지역, 부서내의 평균 급여를 조회해 보세요.
SELECT s.dname, s.loc, avg(s.sal)
FROM (SELECT d.dname, d.loc, e.sal
FROM emp e, dept d
WHERE e.deptno = d.deptno) s
GROUP BY s.dname, s.loc;

SELECT d.dname, d.loc, e.sal
FROM emp e, dept d
WHERE e.deptno = d.deptno;


SELECT c.deptno, d.loc, c.avgsal
FROM dept d inner join (SELECT deptno, avg(sal) as avgsal
FROM emp
GROUP BY deptno) as c
ON d.deptno = c.deptno;
